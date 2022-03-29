# frozen_string_literal: true

N, M = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)
C = gets.chomp.split.map(&:to_i)

A.reverse!
C.reverse!
ans = []

while C.length >= A.length
  quotient = C.first / A.first
  ans << quotient
  A.each_with_index do |a, idx|
    C[idx] -= a * quotient
  end
  C.shift
end

puts ans.reverse!.join(' ')
