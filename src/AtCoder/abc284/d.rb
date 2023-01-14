def main
  t = gets.to_i
  t.times do
    n = gets.to_i
    (2..).each do |i|
      if n%i == 0
        if n%(i**2) == 0
          p = i
          q = n/(i**2)
        else
          p = Math.sqrt(n/i).to_i
          q = i
        end
        puts [p, q].join(" ")
        break
      end
    end
  end
end

main
