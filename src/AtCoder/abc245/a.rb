# frozen_string_literal: true

A, B, C, D = gets.chomp.split.map(&:to_i)

if Time.new(2000, 1, 1, A, B, 0) < Time.new(2000, 1, 1, C, D, 1)
  puts 'Takahashi'
else
  puts 'Aoki'
end
