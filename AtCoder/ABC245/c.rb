# frozen_string_literal: true

require 'set'

N, K = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)
B = gets.chomp.split.map(&:to_i)

available_numbers = Set[A.pop, B.pop]
until A.empty?
  tmp = Set.new
  a = A.pop
  b = B.pop
  available_numbers.each do |n|
    tmp.add(a) if (a - n).abs <= K
    tmp.add(b) if (b - n).abs <= K
  end
  available_numbers = tmp
end

puts available_numbers.size.nonzero? ? 'Yes' : 'No'
