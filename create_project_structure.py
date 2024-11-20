import os

def create_directory_structure():
    # 定义项目结构
    structure = {
        'src': {
            '__init__.py': '',
            'core': {
                '__init__.py': '',
                'vehicle.py': '',
                'road.py': '',
                'intersection.py': '',
                'traffic_light.py': ''
            },
            'simulation': {
                '__init__.py': '',
                'simulator.py': '',
                'path_planning.py': '',
                'traffic_flow.py': ''
            },
            'visualization': {
                '__init__.py': '',
                'gui.py': '',
                'plotting.py': ''
            },
            'utils': {
                '__init__.py': '',
                'helpers.py': ''
            }
        },
        'data': {
            'config': {
                'simulation_params.json': '{}'
            }
        },
        'tests': {
            '__init__.py': '',
            'test_simulation.py': ''
        }
    }
    
    # 创建requirements.txt（如果不存在）
    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w') as f:
            f.write('''numpy>=1.21.0
matplotlib>=3.4.0
PyQt5>=5.15.0
networkx>=2.6.0
''')

    # 递归创建目录和文件
    def create_structure(structure, current_path=''):
        for name, content in structure.items():
            path = os.path.join(current_path, name)
            # 如果是目录
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(content, path)
            # 如果是文件且不存在
            elif content is not None and not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write(content)

    create_structure(structure)
    
    print("项目结构创建完成！")
    print("注意：data/maps 目录下的地图文件已存在，未进行修改。")

if __name__ == '__main__':
    create_directory_structure() 