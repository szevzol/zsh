zsh
===

My zsh settings.

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
