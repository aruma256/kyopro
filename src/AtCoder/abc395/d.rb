N, Q = gets.chomp.split(" ").map(&:to_i)

def main
  pigeon_to_group = (0..N).to_a
  group_to_box = (0..N).to_a
  box_to_group = (0..N).to_a

  Q.times do
    case gets.chomp.split(" ").map(&:to_i)
    in [1, pigeon, box]
      pigeon_to_group[pigeon] = box_to_group[box]
    in [2, box_a, box_b]
      group_a = box_to_group[box_a]
      group_b = box_to_group[box_b]
      group_to_box[group_a], group_to_box[group_b] = box_b, box_a
      box_to_group[box_a], box_to_group[box_b] = group_b, group_a
    in [3, pigeon]
      group = pigeon_to_group[pigeon]
      puts group_to_box[group].to_s
    end
  end
end

main
