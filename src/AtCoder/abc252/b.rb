N, K = gets.chomp.split.map(&:to_i)
A = [0] + gets.chomp.split.map(&:to_i)
B = gets.chomp.split.map(&:to_i)

def main
  max = A.max
  B.each do |idx|
    if A[idx] == max
      puts 'Yes'
      return
    end
  end
  puts 'No'
end

main
