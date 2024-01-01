# MicroBit FNK0045 Tutorial Reimagined

My implementations of various programs in the
[FNK0045 Tutorial.pdf](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_microbit/blob/master/Tutorial.pdf).
The functionality is generally the same as or similar the code in 
[PythonCode](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_microbit/tree/master/Projects/PythonCode)
but different and usually contains debug print
statements and timing information so as to make
it easy to see how the program runs. Therefore I'm
licensing these under my favorite licenses Apache 2.0
and or MIT.

I'm using minicom as the debug console for the microbit.
On my Arch Linux system the microbit shows up as
`/dev/ttyACM0` and I use the `minicom -D /dev/ttyACM0` to
start it. I've also saved the minicom configuration as
`~/.minicom.microbit` and `minicom microbit` can be used
to start it. The configuration file is:
```
$ cat ~/.minirc.microbit 
# Machine-generated file - use setup menu in minicom to change parameters.
pu port             /dev/ttyACM0
```

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.

