from distutils.dir_util import mkpath
from os import path

class Configuration:

    def __init__(self, mode='dev',
                 work_dir='~/mark0',
                 log_file='mark0_log.json'):
        self.work_dir = work_dir
        self.backup_dir = path.sep.join([work_dir, 'backups'])
        mkpath(self.backup_dir)
        self.log_file = path.sep.join([work_dir, log_file])

        devices_run_dir = '/var/run/mark0'
        devices_run_dir = path.sep.join([work_dir, 'run', 'mark0'])
        mkpath(devices_run_dir)
        self.devices_sock = path.sep.join([
            devices_run_dir,
            'devices_d_socket'
        ])

        self.backend = {
            'type': 'aws',
            'media_storage': {
                'type': 's3',
                'endpoint': 'plant-data-mark0',
            },
            'data_storage': {
                'type': 'dynamodb',
                'endpoint': 'mark0_observations',
                'extra': {
                    'reserved_character': '#',
                }
            }
        }
