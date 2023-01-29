N, X = gets.split.map(&:to_i)
AB = N.times.map{gets.split.map(&:to_i)}

def main
  dp = Array.new(size=X+1, val=false)
  dp[0] = true
  AB.each do |price, count|
    dpn = dp.clone
    (0..X).each do |x|
      next unless dp[x]
      (1..count).each do |mul|
        nx = x + price * mul
        break if nx > X
        dpn[nx] = true
      end
    end
    dp = dpn
  end
  if dp[X]
    puts 'Yes'
  else
    puts 'No'
  end
end

main
