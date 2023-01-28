def main
  n, a, b = gets.split.map(&:to_i)
  s = gets.chomp.chars
  ans = 10**20
  n.times do |i|
    score = i*a
    (0...(n/2)).each do |j|
      score += b if s[j] != s[n-1-j]
    end
    ans = [ans, score].min
    s.push s.shift
  end
  puts ans
end

main
