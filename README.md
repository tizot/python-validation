# Using meta-programming to validate data

This repo contains the code illustrating the blog post: https://camillemasset.fr/runtime-type-validation/

The commits correspond to progressive steps in the development of the mini validation framework:
- the tag `demo-start` identifies the initial code (without any validation);
- the tag `demo-end` identifies the end of the development;
- by using the alias `git next` (cf. below), we can go through the development of the project, step by step.

```shell
git config alias.next '!git checkout `git rev-list HEAD..demo-end | tail -1`'
```
