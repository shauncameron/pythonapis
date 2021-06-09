from ReMark.Lexer import *
from ReMark.Compiler import *
import yaml

""" 
Private License (Copyright Shaun Cameron)
author/s: Shaun Cameron, Gary Kong ( In spirit )
creation: 08/06/2021 - 08/06/2021
requires: ReMark [ Regex, <Grammar Dictionary> ], <Grammar Dictionary>"grammar.yaml"
"""

usedIDS = []

tokenizer = Lexer(yaml.load(open('./ReMark/grammar.yaml', 'r').read(), Loader=yaml.FullLoader))

def compile(remark: str = "**Hello World**", target=None, output=True):

    import datetime
    from random import randint

    while (cid := f'REMARK_COMPILE(id={randint(1, 100000)})') not in usedIDS:

        usedIDS.append(cid)

    creation = f"""({datetime.datetime.now()} :: {len(remark)} :: {cid})"""

    if output:

        print(f"""{creation} -> Began creating @ {datetime.datetime.now()}\n---""")

        print(f"""{creation} -> Started making tokens @ {datetime.datetime.now()}""")

    tokens = tokenizer.tokenize(remark)

    if output:

        print(f"""{creation} -> Finished making tokens @ {datetime.datetime.now()}""")

    compiler = Compiler(tokens)

    if output:

        print(f"""{creation} -> Began compiling @ {datetime.datetime.now()}""")

    compiled = compiler.compile()

    if output:

        print(f"""{creation} -> Finished compiling @ {datetime.datetime.now()}""")

    if target is not None and target.endswith('.html'):

        open(target, 'w').write(compiled)

        if output:

            print(f"""{creation} -> Wrote to {target} @ {datetime.datetime.now()}""")

    return compiled

def interpreter(exit_command="$exit"):

    results = []

    while True:

        if (string := input('ReMark << ')) == exit_command:

            break

        result = compile(string, '', False)

        print('ReMark Result >> ' + result)

        results.append(result)

    return results
