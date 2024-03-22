fly apps create -o personal stdout-stderr # or choose another name 
fly deploy -a stdout-stderr
# wait a minute
fly logs -a stdout-stderr

Expected:
This is stdout, 1711134958.920852
This is stderr, 1711134958.920852
This is stdout, 1711134960.9225109
This is stderr, 1711134960.9225109

Actual:
2024-03-22T19:30:55Z app[28749d3c02dee8] yul [info]This is stderr, 1711135855.712613
2024-03-22T19:30:57Z app[e286504df37238] yul [info]This is stderr, 1711135857.379489
2024-03-22T19:30:57Z app[28749d3c02dee8] yul [info]This is stderr, 1711135857.7147043
2024-03-22T19:30:59Z app[e286504df37238] yul [info]This is stderr, 1711135859.3815942
2024-03-22T19:30:59Z app[28749d3c02dee8] yul [info]This is stderr, 1711135859.7168012



