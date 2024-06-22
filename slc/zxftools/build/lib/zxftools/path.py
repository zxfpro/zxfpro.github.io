import itertools
import os


from pathlib import Path as pPath

class Path(object):
    """
    处理路径的所有问题
    """
    def __init__(self, path: str):
        """
        rename_file
        rename_dir(self, name) -> str
        search_suffix(self,file:str = '*.ipynb') -> list
        abs(self) -> str
        subfiles(self) -> str
        create(self) -> None
        add_count(self) -> str
        subfiles_iter(self, fn=lambda x: not x.startswith('.')) -> iter
        get_project_root(self) -> str
        moveto(to_file: str) -> None
        movesto(to_dir: str) -> None
        """
        self.path2 = pPath(path)
        self.path = str(self.path2)

    def __repr__(self):
        return self.path

    def exist(self):
        """
        是否存在
        """
        # return os.path.exists(self.path)
        return self.path2.exists()

    def mkdir(self):
        """
        创建路径
        """
        self.path2.mkdir(parents=True, exist_ok=True)


    def get_project_root(self) -> str:
        """
        获取项目根目录
        """
        current_path = self.path
        while True:
            if (
                    (current_path / ".git").exists()
                    or (current_path / ".project_root").exists()
                    or (current_path / ".gitignore").exists()
            ):
                # use metagpt with git clone will land here
                # logger.info(f"PROJECT_ROOT set to {str(current_path)}")
                return current_path
            parent_path = current_path.parent
            if parent_path == current_path:
                # use metagpt with pip install will land here
                cwd = os.getcwd()
                # logger.info(f"PROJECT_ROOT set to current working directory: {str(cwd)}")
                return cwd
            current_path = parent_path
        return current_path

    def rename(self,name):
        self.path2.rename(name)

    def abs(self) -> str:
        """
        部分路径 -》 完整路径
        """
        return self.path2.absolute()

    def subfiles(self) -> str:
        """
        列出子文件
        """
        return os.listdir(self.path)

    def add_count(self) -> str:
        """
        添加计数
        """
        if not os.path.exists(self.path):
            # print(f'{self.path},is not exists')
            return self.path

        count = 0
        name = self.path.split('/')[-1]
        paths = '/'.join(self.path.split('/')[:-1])
        files = os.listdir(paths or None)
        for file in files:
            if file.startswith(name):
                count = count + 1

        if os.path.isdir(self.path):
            if paths:
                return paths + '/' + name + '_' + str(count)
            else:
                return name + '_' + str(count)
        elif os.path.isfile(self.path):
            head, sufflx = name.split('.')
            if paths:
                return paths + '/' + head + '_' + str(count) + '.' + sufflx
            else:
                return head + '_' + str(count) + '.' + sufflx

    def subfiles_iter(self, fn=lambda x: not x.startswith('.')) -> iter:
        """
        子文件迭代器
        """
        try:
            assert os.path.isfile(self.path)
        except:
            print(f'{self.path},is not dir')

        for path in itertools.takewhile(fn, os.listdir(self.path)):
            full_path = os.path.join(self.path, path)
            yield full_path


__all__ = ['Path']