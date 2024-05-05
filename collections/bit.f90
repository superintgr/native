program bit_inquiry
    use, intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
    !! why not int24?
    implicit none
    integer :: i
    integer(kind = int8) :: byte
    integer(kind = int8), allocatable :: array_x(:), array_y(:)
        !! basic usages
        write(*, *) 'bge(-127, +127) =', bge(-127, 127)
        write(*, *) 'bge(b"0001, 2) =', bge("1", 2)
        !! elemental kind
        write(*, *) 'Compare array sequence [-128, -0, +0, 127] to 127'
        write(*, *) bge(int([-128, -0, +0, 127], kind=int8), 127_int8)
