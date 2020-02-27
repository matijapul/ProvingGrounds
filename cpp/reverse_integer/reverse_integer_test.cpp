#include "reverse_integer.hpp"
#include "gtest/gtest.h"

/*
This test calls function "reverse" defined in reverse_integer.hpp
which recieves an integer as input and returns its reversed value.
You can change this test to suit your implementation (for example
if you implemented the reverse function as a method within a class).
*/

TEST(reverseInteger, checkReverse){
  EXPECT_EQ(reverse(0), 0);
  EXPECT_EQ(reverse(123), 321);
  EXPECT_EQ(reverse(-123), -321);
  EXPECT_EQ(reverse(120), 21);
}