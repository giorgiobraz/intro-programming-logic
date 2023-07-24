import intro

def test_countdown_rocket(capsys):
    intro.countdown_rocket()
    captured = capsys.readouterr()
    assert captured.out.strip() == "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n0\nFogo!"