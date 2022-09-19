import hog
leader, message = hog.announce_lead_changes(5, 0)
print(message)
    #Player 0 takes the lead by 5
leader, message = hog.announce_lead_changes(5, 12, leader)
print(message)
      #Player 1 takes the lead by 7
leader, message = hog.announce_lead_changes(8, 12, leader)
print(leader, message)
      #1 None
leader, message = hog.announce_lead_changes(8, 13, leader)
leader, message = hog.announce_lead_changes(15, 13, leader)
print(message)
      #Player 0 takes the lead by 2
