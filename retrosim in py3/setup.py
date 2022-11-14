from distutils.core import setup

# 这是一个和根目录相关的安装文件的列表，列表中setup.py更具体)


setup(name="retrosim",
      version="0.0.1",
      description="hx",
      author="hx",
      author_email="meli.ssa@sjtu.edu.cn",
      # Name the folder where your packages live:
      # (If you have other packages (dirs) or modules (py files) then
      # put them into the package directory - they will be found recursively.)
      packages=['rdchiral', 'retrosim'])
# 'package' package must contain files (see list above)
# I called the package 'package' thus cleverly confusing the whole issue...
# This dict maps the package name =to=> directories
# It says, package *needs* these files.
# 'runner' is in the root.      long_description="""Really long text here.""")
#
# This next part it for the Cheese Shop, look a little down the page.
# classifiers = []