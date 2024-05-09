# Shell Script Embed Binary

This is a template shell script that can be used to embed binary executables to 
execute on invocation. It allows one to create "install scripts" in a portable
manner. 

To load your binary, use the following command
```sh
$ tar -cjf - path/to/binary | base64 | fold >> embed.sh
```

You should replace the value of the `EXE_NAME` variable in the script with the 
name of executable you passed to the command above.

This will base64 encode the bzip compressed binary and append it to the end of
the file. Ensure that the appended base64 data sits exactly one line below the 
`__PAYLOAD__` line.

Given that this is a template script, you can add your own code to the script. 
Have your script call the `_exec_payload()` method when you wish to execute the
binary. This method does not return, and replaces the current process with your
binary. Thus anything you write after this call will not be executed. You may
pass function arguments to `_exec_payload()` and they will passed as command-
line arguments to your loaded binary.

