import subprocess
import  pytest
from src.pgbackup import pgdump


url = "postgres://user@example.com:5432/db_name"
driver_flag = "--driver"
driver_value = "local"
driver_unknown_value = "digital_ocean"
destination = "/some/backup/path"


def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)


def test_dump_handles_os_error(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
