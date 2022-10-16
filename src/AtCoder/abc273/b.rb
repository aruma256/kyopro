X, K = gets.chomp.split.map(&:to_i)

r = Rational(X)
K.times do
  r = Rational((r / 10).round)
end

puts r.to_i * 10**K
