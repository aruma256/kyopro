N, M, K = gets.chomp.split.map(&:to_i)
MOD = 998244353

a = Array.new(K+1, 0)
a[0] = 1
an = Array.new(K+1, 0)

N.times do
  (0..K).each do |v|
    (1..M).each do |i|
      if v+i <= K
        an[v+i] += a[v]
      else
        break
      end
    end
  end
  a, an = an, a
  an.fill(0)
  a.map!{ |v| v % MOD }
end

puts a.sum % MOD
