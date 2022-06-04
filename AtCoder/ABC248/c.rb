n, m, k = gets.chomp.split.map(&:to_i)

dp = [0] * (k+1)
ndp = [0] * (k+1)

dp[0] = 1

n.times do
  (0...k).each do |orig|
    (1..m).each do |d|
      break if orig+d > k
      ndp[orig+d] += dp[orig]
    end
  end
  dp, ndp = ndp, dp
  dp.map{ |i| i % 998244353 }
  ndp.fill(0)
end

puts dp.sum % 998244353
