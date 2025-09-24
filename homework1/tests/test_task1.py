# Set up pytest case that verifies the output of task1 script.
from task1 import main

def test_hello_world_output(capsys):
    main()
    captured = capsys.readouterr() 
    assert captured.out.strip() == "Hello, World!"