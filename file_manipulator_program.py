import sys

pathname = sys.argv[2]

#'reverse'コマンド実行時の処理
if sys.argv[1] == 'reverse':
    with open(pathname) as f:
        contents = f.read()

    reversed_contents = contents[::-1]

    with open('output.txt', 'w') as f:
        f.write(reversed_contents)

#'copy'コマンド実行時の処理
if sys.argv[1] == 'copy':
    with open(pathname) as f:
        contents = f.read()
        
    with open('output.txt', 'w') as f:
        f.write(contents)

#'duplicate'コマンド実行時の処理
if sys.argv[1] == 'duplicate-contents':
    with open(pathname) as f:
        contents = f.read()
    
    count = int(sys.argv[3])
    duplicated_contents = contents * count

    with open(pathname, 'w') as f:
        f.write(duplicated_contents)
        
#'replace-string'コマンド実行時の処理
if sys.argv[1] == 'replace-string':
    with open(pathname) as f:
        contents = f.read()
        
    replaced_contents = contents.replace('needle', 'newstring')

    with open(pathname, 'w') as f:
        f.write(replaced_contents) 