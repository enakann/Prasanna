import pathlib
import os
p=pathlib.Path(__file__).resolve().parent
print(p)



def get_params_for(file_name, dir_path, env_name):
    """Function to create a ros2 launch system compatible parameter array for a given parameter file location.

    Keyword Arguments:
        file_name : The name of the launch file, e.g 'param.yaml'

        dir_path : The path to the directory containing the parameter file

        env_name : Arbitrary environment variable name for temporarily storing the dir_path

    As of now, the dcrt launch system does not provide a simple way to use launch files. This function is a
    workaround and can be removed once a simpler API is available for loading parameter files.

    Returns:
        The ros2 launch system compatible params array
    """
    params_file_path = dir_path / file_name
    os.environ[env_name] = str(dir_path)
    params = [
        params_file_path,
        str(params_file_path),
        [os.environ.get(env_name), os.sep, file_name],
    ]
    return params


cur_dir = pathlib.Path(__file__).resolve().parent
sandbox_dir = cur_dir.parent.parent.parent.parent

test_framework_params = get_params_for(file_name='simulation.params.yaml',
                                       dir_path=cur_dir,
                                       env_name='LAUNCH_DIR_PATH')

vehicle_control_params = get_params_for(file_name='VtdAudiA6.yaml',
                                        dir_path=sandbox_dir / 'install/share/vehicle_control/param/',
                                        env_name='VEHICLE_CONTROL_PATH')

vehicle_interface_params = get_params_for(file_name='VtdAudiA6.yaml',
                                          dir_path=sandbox_dir / 'install/share/vehicle_interface_vtd/param/',
                                          env_name='VEHICLE_INTERFACE_PATH')

print(test_framework_params)
print(vehicle_control_params)
print(vehicle_interface_params)