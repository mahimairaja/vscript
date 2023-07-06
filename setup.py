from setuptools import setup

setup(
    name="vscript",
    version="0.1",
    packages=["vscript"],
    install_requires=["click", "ultralytics", \
        "supervision","validators", \
        "pyspellchecker", "lark", ],
    entry_points="""
        [console_scripts]
        vscript=vscript.main:vscript_cli
    """
)