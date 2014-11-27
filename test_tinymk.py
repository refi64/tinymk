import pytest, tempfile, os, time
from tinymk import *

@task()
def t():
    print('123')

def test_run():
    assert run('echo 123', shell=True, get_output=True)[0] == '123\n'
    with pytest.raises(SystemExit):
        run('ls nonexistent_directory')

def test_run_d():
    with tempfile.NamedTemporaryFile() as dep,\
         tempfile.NamedTemporaryFile() as out:
        time.sleep(0.1) # make sure dep is newer than out
        dep.write(b'123')
        dep.flush()
        run_d(out.name, dep.name, 'cp %s %s' % (dep.name, out.name))
        assert out.read() == b'123'
        t = os.path.getmtime(out.name)
        run_d(out.name, dep.name, 'cp %s %s' % (dep.name, out.name))
        assert os.path.getmtime(out.name) == t

def test_task_and_invoke(capsys):
    qinvoke('t')
    assert capsys.readouterr()[0] == '123\n'
    invoke('t')
    assert capsys.readouterr()[0] == 'Running task t...\n123\n'
