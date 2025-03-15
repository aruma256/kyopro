N = gets.to_i
A = gets.chomp.split(" ").map(&:to_i)

def main
  (N-1).times do |i|
    if A[i] >= A[i+1]
      puts "No"
      exit
    end
  end

  puts "Yes"
end

main
