zsh
===

My zsh configuration.

This repository serves as a portable configuration for me.
Feel free to use it but please beware of the fact that I didn't prepared it to be used by others.

Set up
------

* Clone the repository. I usually clone into ~/etc. Directory ~/etc/zsh will be created with the content of the repository.
* Create ~/.zprofile. This should contain setting of ZSH_HOME  and sourcing the zprofile from the repository. In fact ZSH_HOME is the path of the repository.

```sh
export ZSH_HOME="$HOME/etc/zsh"
. "$ZSH_HOME/rc/zprofile"
```

* Create ~/.zshrc which will be a symbolic link to the zshrc inside the repository:

```sh
ln -s ~/etc/zsh/rc/zshrc ~/.zshrc
```

The private files
-----------------

The rc/zprofile and rc/alias files will source their private counterparts zprofile.private and alias.private. These private files contain settings which I don't want to share on GitHub and are very environment specific.
