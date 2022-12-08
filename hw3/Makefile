all: one two three

one:
	touch ./one

other_one:
	@echo "other_one"
	@touch ./one

two: ./one
	touch ./two

three: ./one ./two
	touch ./three

clear:
	rm ./one
	rm ./two
	rm ./three

clean: clear
