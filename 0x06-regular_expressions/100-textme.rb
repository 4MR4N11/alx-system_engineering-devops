#!/usr/bin/env ruby
sender =  ARGV[0].scan(/(?<=from:)(.*?)(?=\])/).join
receiver = ARGV[0].scan(/(?<=to:)(.*?)(?=\])/).join
flags = ARGV[0].scan(/(?<=flags:)(.*?)(?=\])/).join
result = sender + "," + receiver + "," + flags
puts result