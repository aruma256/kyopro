# frozen_string_literal: true

require 'set'

N = gets.chomp.to_i
A = Set.new gets.chomp.split.map(&:to_i)
(0..).each do |i|
  unless A.include?(i)
    puts i
    break
  end
end
