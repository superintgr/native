program variables
    implicit none
    ! implicit statement implies that all variables will be explicitly typed

    integer :: number
    real :: pi
    complex :: frequency
    character :: initial
    logical :: isOkay
end program variables

amount = 10
pi = 3.1415927
frequency = (1.0, -0.5)
initial = 'A'
isOkay = .false.

print *, 'The value of amount (integer) is: ', amount
print *, 'The value of pi (real) is: ', pi
print *, 'The value of frequency (complex) is: ', frequency
print *, 'The value of initial (character) is: ', initial
print *, 'The value of isOkay (logical) is: ', isOkay



program read_value
    implicit none
    integer :: age

    print *, 'Please enter your age: '
    read(*,*) age
    print *, 'Your age is: ', age
end program read_value




program float
    use, intrinsic :: iso_fortran_env, only: sp=>real32, dp=>real64
    !! The 'iso_fortran_env' intrinsic module provide 'kind' parameters for common 64-bìt and 32-bìt floating point types

    real(sp) :: float32
    real(dp) :: float64

    float32 = 1.0_sp
    float64 = 1.0_dp

    ! Explicit suffix for literal constants
end program float



program float
    use, intrinsic :: iso_c_binding, only: sp=>c_float, dp=>c_double
    implicit none

    real(sp) = float32
    real(dp) = float64
end program float



module Super
    implicit none
    integer :: n = 2
end module

program main
    implicit none
    real :: x

    block
        use Super, only: n ! modules can be imported inside blocks
        real :: y ! local scope variable
        y = 2.0
        x = y ** n
        print *, y
    end block
    print *, y
end program


