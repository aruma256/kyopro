N, K = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)

def nibutan(ok, ng, &block)
  while (ok - ng).abs > 1
    mid = (ok + ng) / 2
    if yield(mid)
      ok = mid
    else
      ng = mid
    end
  end
  ok
end

def main
  ans = nibutan(A.max, 0) do |target_length|
    count = 0
    A.each do |a|
      count += (a - 1) / target_length
    end
    count <= K
  end
  puts ans
end

main()
