import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('./.venv/lib/python3.8/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"editor":{"mode":"preview","agent":"vscode","version":"1.0.73"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://3000-breathecode-pythonflask-nd6k1l2733a.ws-us83.gitpod.io","contact":"https://github.com/learnpack/learnpack/issues/new","language":"auto","autoPlay":true,"projectType":"tutorial","grading":"incremental","exercisesPath":".learn/exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"title":"Todo List API with Python Flask Interactive","slug":"python-flask-api-tutorial","status":"published","solution":"https://github.com/breatheco-de/todo-list-api-interactive/tree/solution","repository":"https://github.com/breatheco-de/python-flask-api-tutorial","preview":"https://github.com/breatheco-de/python-flask-api-tutorial/blob/master/.learn/assets/preview.png?raw=true","duration":6,"difficulty":"easy","videoSolutions":false,"bugsLink":"https://github.com/learnpack/learnpack/issues/new","description":"Create a Todo list API Interactively using Python language and the Flask Framework","technologies":["python","terminal","command-line","APIs","REST"],"translations":[]}')])
