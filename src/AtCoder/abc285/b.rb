N = gets.to_i
S = (" " + gets.chomp).chars

def main
  (1...N).each do |i|
    ans = 0
    (1..).each do |k|
      if k+i <= N && S[k]!=S[k+i]
        ans += 1
      else
        break
      end
    end
    puts ans
  end
end

main
