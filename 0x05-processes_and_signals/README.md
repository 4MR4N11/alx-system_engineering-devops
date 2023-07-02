# 0x05. Processes and signals

This project is about processes and signals in bash.

## Files

- [0-what-is-my-pid](0-what-is-my-pid) - Bash script that displays its own PID.

- [1-list_your_processes](1-list_your_processes) - Bash script that displays a list of currently running processes.

- [2-show_your_bash_pid](2-show_your_bash_pid) - Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

- [3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) - Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

- [4-to_infinity_and_beyond](4-to_infinity_and_beyond) - Bash script that displays To infinity and beyond indefinitely.

- [5-dont_stop_me_now](5-dont_stop_me_now) - Bash script that stops 4-to_infinity_and_beyond process using kill.

- [6-stop_me_if_you_can](6-stop_me_if_you_can) - Bash script that stops 4-to_infinity_and_beyond process without using kill or killall.

- [7-highlander](7-highlander) - Bash script that displays:
  - To infinity and beyond indefinitely
  - With a sleep 2 in between each iteration
  - I am invincible!!! when receiving a SIGTERM signal

- [8-beheaded_process](8-beheaded_process) - Bash script that kills the process 7-highlander.

- [100-process_and_pid_file](100-process_and_pid_file) - Bash script that:
  - Creates the file /var/run/myscript.pid containing its PID
  - Displays To infinity and beyond indefinitely
  - Displays I hate the kill command when receiving a SIGTERM signal
  - Displays Y U no love me?! when receiving a SIGINT signal
  - Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
