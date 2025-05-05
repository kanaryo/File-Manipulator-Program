import sys

def validate_args(expected_args):
    if len(sys.argv) < expected_args:
        print(f"Error: Expected at least {expected_args} arguments, but got {len(sys.argv)}.")
        sys.exit(1)

# コマンドとファイルパスの取得（最低でも2つの引数が必要）
if len(sys.argv) < 3:
    print("Usage:")
    print("  reverse <inputfile>")
    print("  copy <inputfile>")
    print("  duplicate-contents <inputfile> <count>")
    print("  replace-string <inputfile>")
    sys.exit(1)
    
pathname = sys.argv[2]

#'reverse'コマンド実行時の処理
if sys.argv[1] == 'reverse':
    validate_args(4)
    with open(pathname) as f:
        contents = f.read()

    reversed_contents = contents[::-1]

    with open('output.txt', 'w') as f:
        f.write(reversed_contents)

#'copy'コマンド実行時の処理
if sys.argv[1] == 'copy':
    validate_args(4)
    with open(pathname) as f:
        contents = f.read()
        
    with open('output.txt', 'w') as f:
        f.write(contents)

#'duplicate'コマンド実行時の処理
if sys.argv[1] == 'duplicate-contents':
    validate_args(4)
    try:
        count = int(sys.argv[3])
    except ValueError:
        print("Error: The duplication count must be an integer.")
        sys.exit(1)
    with open(pathname) as f:
        contents = f.read()
    
    duplicated_contents = contents + contents * count

    with open(pathname, 'w') as f:
        f.write(duplicated_contents)
        
#'replace-string'コマンド実行時の処理
if sys.argv[1] == 'replace-string':
    validate_args(5)
    with open(pathname) as f:
        contents = f.read()
        
    replaced_contents = contents.replace('needle', 'newstring')

    with open(pathname, 'w') as f:
        f.write(replaced_contents) 