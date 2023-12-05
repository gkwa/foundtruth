rm -rf /tmp/foundtruth
rm -f /tmp/foundtruth.tar
rm -f /tmp/filelist.txt

pytest >pytest.log 2>&1
rg --no-ignore --files . |
    grep -iE 'test_skeleton.py|src|pytest.log' |
    grep -viE '__init__.py' |
    grep -viE '__pycache' |
    grep -vF .egg |
    tee /tmp/filelist.txt

tar -cf /tmp/foundtruth.tar -T /tmp/filelist.txt
mkdir -p /tmp/foundtruth
tar xf /tmp/foundtruth.tar -C /tmp/foundtruth
rg --files /tmp/foundtruth
txtar-c /tmp/foundtruth | pbcopy
