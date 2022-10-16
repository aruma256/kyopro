S = ' ' + gets.chomp
N = S.size

chokudai = ' chokudai'

dp = Array.new(N) { [1] + [0] * 8 }
dp[0][0] = 1

(1...N).each do |i|
  (1...chokudai.length).each do |ci|
    z = dp[i-1][ci]
    if S[i] == chokudai[ci]
      z += dp[i-1][ci-1]
    end
    dp[i][ci] = z % 1000000007
  end
end

puts dp.last.last
