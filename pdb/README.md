Pdb Commands

Begin the debugger

```
python-mpdb<name>.py[args]
```
View a list of commands, or view help for a specific command

```
help [command]
```

Within a python file, to begin the debugger at this line when the file is run normally

```python
importpdb
...
pdb.set_trace()
```

List 11 lines surrounding the current line
```
l(ist)
```
Display the file and line number of the current line
'''
w(here)
'''

Execute the current line
```
n(ext)
```
Step into functions called at the current line
```
s(tep)
```
Execute until the current function’s return is encountered

```
r(eturn) 
```
Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands
```
w(where)
```
Move the current frame one level up in the stack trace (to an older frame)
```
u(up)
```
Move the current frame one level down in the stack trace (to a newer frame).
```
d(down)
```
Create a breakpoint at line [#]
```
b(reak) [#]
```
List breakpoints and their indices
```
b(break)
```
Execute until a breakpoint is encountered
```
c(ontinue)
```
Clear breakpoint of index [#]
```
clear[#]
```
Print value of the variable <name>
```
p <name>
```
Execute the expression <expr> NOTE: this acts just like a python interpreter
```
!<expr>
```
Restart the debugger with sys.argv arguments [args]
```
run [args] 
```
Exit the debugger
```
q(uit)
```
