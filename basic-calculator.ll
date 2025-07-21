; ModuleID = 'basic-calculator.c'
source_filename = "basic-calculator.c"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128-Fn32"
target triple = "arm64-apple-macosx15.0.0"

%struct.Token = type { i32, i64, i64 }

@buf = global ptr null, align 8
@buf_size = global i64 0, align 8
@buf_count = global i64 0, align 8
@col_no = global i64 0, align 8
@current = global ptr null, align 8
@current_token = global %struct.Token zeroinitializer, align 8
@has_error = global i8 0, align 1
@.str = private unnamed_addr constant [35 x i8] c"Basic Calculator\0ACtrl-C/D to exit\0A\00", align 1
@.str.1 = private unnamed_addr constant [23 x i8] c"Enter an expresssion: \00", align 1
@__stdinp = external global ptr, align 8
@.str.2 = private unnamed_addr constant [29 x i8] c"error: incomplete expression\00", align 1
@.str.3 = private unnamed_addr constant [7 x i8] c"unused\00", align 1
@.str.4 = private unnamed_addr constant [5 x i8] c"%ld\0A\00", align 1
@.str.5 = private unnamed_addr constant [8 x i8] c"realloc\00", align 1
@.str.6 = private unnamed_addr constant [31 x i8] c"error: unexpected character %c\00", align 1
@.str.7 = private unnamed_addr constant [20 x i8] c"symbol unrecognized\00", align 1
@.str.8 = private unnamed_addr constant [26 x i8] c"error: cannot divide by 0\00", align 1
@.str.9 = private unnamed_addr constant [37 x i8] c"the following divisor evaluates to 0\00", align 1
@.str.10 = private unnamed_addr constant [37 x i8] c"error: unmatched opening parentheses\00", align 1
@.str.11 = private unnamed_addr constant [41 x i8] c"possibly missing closing parentheses ')'\00", align 1
@.str.12 = private unnamed_addr constant [1 x i8] zeroinitializer, align 1
@.str.13 = private unnamed_addr constant [15 x i8] c"unexpected EOF\00", align 1
@.str.14 = private unnamed_addr constant [24 x i8] c"error: unexpected token\00", align 1
@.str.15 = private unnamed_addr constant [51 x i8] c"expected parenthesized expression or numeric value\00", align 1
@__stderrp = external global ptr, align 8
@.str.16 = private unnamed_addr constant [6 x i8] c"\1B[33m\00", align 1
@.str.17 = private unnamed_addr constant [5 x i8] c"\1B[0m\00", align 1
@.str.18 = private unnamed_addr constant [6 x i8] c"\1B[31m\00", align 1
@.str.19 = private unnamed_addr constant [6 x i8] c"\1B[32m\00", align 1

; Function Attrs: nounwind ssp uwtable(sync)
define i32 @main(i32 noundef %0, ptr noundef %1) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca ptr, align 8
  %6 = alloca i32, align 4
  %7 = alloca i64, align 8
  %8 = alloca %struct.Token, align 8
  store i32 0, ptr %3, align 4
  store i32 %0, ptr %4, align 4, !tbaa !6
  store ptr %1, ptr %5, align 8, !tbaa !10
  %9 = call i32 (ptr, ...) @printf(ptr noundef @.str)
  br label %10

10:                                               ; preds = %2, %46
  %11 = call i32 (ptr, ...) @printf(ptr noundef @.str.1)
  call void @llvm.lifetime.start.p0(i64 4, ptr %6) #9
  br label %12

12:                                               ; preds = %20, %10
  %13 = load ptr, ptr @__stdinp, align 8, !tbaa !10
  %14 = call i32 @fgetc(ptr noundef %13)
  store i32 %14, ptr %6, align 4, !tbaa !6
  %15 = icmp ne i32 %14, -1
  br i1 %15, label %16, label %23

16:                                               ; preds = %12
  %17 = load i32, ptr %6, align 4, !tbaa !6
  %18 = icmp eq i32 %17, 10
  br i1 %18, label %19, label %20

19:                                               ; preds = %16
  br label %23

20:                                               ; preds = %16
  %21 = load i32, ptr %6, align 4, !tbaa !6
  %22 = trunc i32 %21 to i8
  call void @buffer_write_char(i8 noundef signext %22)
  br label %12, !llvm.loop !12

23:                                               ; preds = %19, %12
  %24 = load i32, ptr %6, align 4, !tbaa !6
  %25 = icmp eq i32 %24, -1
  br i1 %25, label %29, label %26

26:                                               ; preds = %23
  %27 = load i64, ptr @buf_size, align 8, !tbaa !15
  %28 = icmp eq i64 %27, 0
  br i1 %28, label %29, label %30

29:                                               ; preds = %26, %23
  call void @exit(i32 noundef 0) #10
  unreachable

30:                                               ; preds = %26
  call void @llvm.lifetime.start.p0(i64 8, ptr %7) #9
  %31 = call i64 @parse_expression()
  store i64 %31, ptr %7, align 8, !tbaa !15
  %32 = call zeroext i1 @match_token(i32 noundef 7)
  br i1 %32, label %39, label %33

33:                                               ; preds = %30
  call void @peek_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %8)
  %34 = getelementptr inbounds %struct.Token, ptr %8, i32 0, i32 2
  %35 = load i64, ptr %34, align 8, !tbaa !17
  %36 = load ptr, ptr @buf, align 8, !tbaa !10
  %37 = call i64 @strlen(ptr noundef %36) #9
  %38 = add i64 %37, 1
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %35, i64 noundef %38, ptr noundef @.str.2, ptr noundef @.str.3)
  br label %46

39:                                               ; preds = %30
  %40 = load i8, ptr @has_error, align 1, !tbaa !19, !range !21, !noundef !22
  %41 = trunc i8 %40 to i1
  br i1 %41, label %45, label %42

42:                                               ; preds = %39
  %43 = load i64, ptr %7, align 8, !tbaa !15
  %44 = call i32 (ptr, ...) @printf(ptr noundef @.str.4, i64 noundef %43)
  br label %45

45:                                               ; preds = %42, %39
  br label %46

46:                                               ; preds = %45, %33
  call void @buffer_reset()
  store i8 0, ptr @has_error, align 1, !tbaa !19
  call void @llvm.lifetime.end.p0(i64 8, ptr %7) #9
  call void @llvm.lifetime.end.p0(i64 4, ptr %6) #9
  br label %10, !llvm.loop !23
}

declare i32 @printf(ptr noundef, ...) #1

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(i64 immarg, ptr nocapture) #2

declare i32 @fgetc(ptr noundef) #1

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @buffer_write_char(i8 noundef signext %0) #0 {
  %2 = alloca i8, align 1
  store i8 %0, ptr %2, align 1, !tbaa !24
  %3 = load i64, ptr @buf_count, align 8, !tbaa !15
  %4 = add i64 %3, 1
  %5 = load i64, ptr @buf_size, align 8, !tbaa !15
  %6 = icmp uge i64 %4, %5
  br i1 %6, label %7, label %22

7:                                                ; preds = %1
  %8 = load i64, ptr @buf_size, align 8, !tbaa !15
  %9 = icmp eq i64 %8, 0
  br i1 %9, label %10, label %11

10:                                               ; preds = %7
  store i64 8, ptr @buf_size, align 8, !tbaa !15
  br label %14

11:                                               ; preds = %7
  %12 = load i64, ptr @buf_size, align 8, !tbaa !15
  %13 = mul i64 %12, 2
  store i64 %13, ptr @buf_size, align 8, !tbaa !15
  br label %14

14:                                               ; preds = %11, %10
  %15 = load ptr, ptr @buf, align 8, !tbaa !10
  %16 = load i64, ptr @buf_size, align 8, !tbaa !15
  %17 = call ptr @realloc(ptr noundef %15, i64 noundef %16) #11
  store ptr %17, ptr @buf, align 8, !tbaa !10
  %18 = load ptr, ptr @buf, align 8, !tbaa !10
  %19 = icmp ne ptr %18, null
  br i1 %19, label %21, label %20

20:                                               ; preds = %14
  call void @perror(ptr noundef @.str.5) #12
  call void @exit(i32 noundef 1) #10
  unreachable

21:                                               ; preds = %14
  br label %22

22:                                               ; preds = %21, %1
  %23 = load i8, ptr %2, align 1, !tbaa !24
  %24 = load ptr, ptr @buf, align 8, !tbaa !10
  %25 = load i64, ptr @buf_count, align 8, !tbaa !15
  %26 = add i64 %25, 1
  store i64 %26, ptr @buf_count, align 8, !tbaa !15
  %27 = getelementptr inbounds i8, ptr %24, i64 %25
  store i8 %23, ptr %27, align 1, !tbaa !24
  %28 = load ptr, ptr @buf, align 8, !tbaa !10
  %29 = load i64, ptr @buf_count, align 8, !tbaa !15
  %30 = getelementptr inbounds i8, ptr %28, i64 %29
  store i8 0, ptr %30, align 1, !tbaa !24
  ret void
}

; Function Attrs: noreturn
declare void @exit(i32 noundef) #3

; Function Attrs: nounwind ssp uwtable(sync)
define internal zeroext i1 @match_token(i32 noundef %0) #0 {
  %2 = alloca i1, align 1
  %3 = alloca i32, align 4
  %4 = alloca %struct.Token, align 8
  store i32 %0, ptr %3, align 4, !tbaa !6
  %5 = load i32, ptr @current_token, align 8, !tbaa !25
  %6 = load i32, ptr %3, align 4, !tbaa !6
  %7 = icmp eq i32 %5, %6
  br i1 %7, label %8, label %9

8:                                                ; preds = %1
  call void @llvm.lifetime.start.p0(i64 24, ptr %4) #9
  call void @advance_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %4)
  call void @llvm.lifetime.end.p0(i64 24, ptr %4) #9
  store i1 true, ptr %2, align 1
  br label %10

9:                                                ; preds = %1
  store i1 false, ptr %2, align 1
  br label %10

10:                                               ; preds = %9, %8
  %11 = load i1, ptr %2, align 1
  ret i1 %11
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @error(i64 noundef %0, i64 noundef %1, ptr noundef %2, ptr noundef %3, ...) #0 {
  %5 = alloca i64, align 8
  %6 = alloca i64, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  %9 = alloca ptr, align 8
  %10 = alloca i64, align 8
  %11 = alloca i64, align 8
  store i64 %0, ptr %5, align 8, !tbaa !15
  store i64 %1, ptr %6, align 8, !tbaa !15
  store ptr %2, ptr %7, align 8, !tbaa !10
  store ptr %3, ptr %8, align 8, !tbaa !10
  %12 = load i8, ptr @has_error, align 1, !tbaa !19, !range !21, !noundef !22
  %13 = trunc i8 %12 to i1
  br i1 %13, label %14, label %15

14:                                               ; preds = %4
  br label %117

15:                                               ; preds = %4
  call void @llvm.lifetime.start.p0(i64 8, ptr %9) #9
  call void @llvm.va_start.p0(ptr %9)
  store i8 1, ptr @has_error, align 1, !tbaa !19
  %16 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %17 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %16, ptr noundef @.str.16) #9
  %18 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %19 = load ptr, ptr %7, align 8, !tbaa !10
  %20 = load ptr, ptr %9, align 8, !tbaa !10
  %21 = call i32 @vfprintf(ptr noundef %18, ptr noundef %19, ptr noundef %20) #9
  %22 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %23 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %22, ptr noundef @.str.17) #9
  %24 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %25 = call i32 @putc(i32 noundef 10, ptr noundef %24)
  call void @llvm.lifetime.start.p0(i64 8, ptr %10) #9
  store i64 0, ptr %10, align 8, !tbaa !15
  br label %26

26:                                               ; preds = %63, %15
  %27 = load ptr, ptr @buf, align 8, !tbaa !10
  %28 = load i64, ptr %10, align 8, !tbaa !15
  %29 = getelementptr inbounds i8, ptr %27, i64 %28
  %30 = load i8, ptr %29, align 1, !tbaa !24
  %31 = sext i8 %30 to i32
  %32 = icmp ne i32 %31, 0
  br i1 %32, label %34, label %33

33:                                               ; preds = %26
  call void @llvm.lifetime.end.p0(i64 8, ptr %10) #9
  br label %66

34:                                               ; preds = %26
  %35 = load i64, ptr %10, align 8, !tbaa !15
  %36 = load i64, ptr %5, align 8, !tbaa !15
  %37 = icmp uge i64 %35, %36
  br i1 %37, label %38, label %54

38:                                               ; preds = %34
  %39 = load i64, ptr %10, align 8, !tbaa !15
  %40 = load i64, ptr %6, align 8, !tbaa !15
  %41 = icmp ule i64 %39, %40
  br i1 %41, label %42, label %54

42:                                               ; preds = %38
  %43 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %44 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %43, ptr noundef @.str.18) #9
  %45 = load ptr, ptr @buf, align 8, !tbaa !10
  %46 = load i64, ptr %10, align 8, !tbaa !15
  %47 = getelementptr inbounds i8, ptr %45, i64 %46
  %48 = load i8, ptr %47, align 1, !tbaa !24
  %49 = sext i8 %48 to i32
  %50 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %51 = call i32 @putc(i32 noundef %49, ptr noundef %50)
  %52 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %53 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %52, ptr noundef @.str.17) #9
  br label %62

54:                                               ; preds = %38, %34
  %55 = load ptr, ptr @buf, align 8, !tbaa !10
  %56 = load i64, ptr %10, align 8, !tbaa !15
  %57 = getelementptr inbounds i8, ptr %55, i64 %56
  %58 = load i8, ptr %57, align 1, !tbaa !24
  %59 = sext i8 %58 to i32
  %60 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %61 = call i32 @putc(i32 noundef %59, ptr noundef %60)
  br label %62

62:                                               ; preds = %54, %42
  br label %63

63:                                               ; preds = %62
  %64 = load i64, ptr %10, align 8, !tbaa !15
  %65 = add i64 %64, 1
  store i64 %65, ptr %10, align 8, !tbaa !15
  br label %26, !llvm.loop !26

66:                                               ; preds = %33
  %67 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %68 = call i32 @putc(i32 noundef 10, ptr noundef %67)
  %69 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %70 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %69, ptr noundef @.str.16) #9
  call void @llvm.lifetime.start.p0(i64 8, ptr %11) #9
  store i64 0, ptr %11, align 8, !tbaa !15
  br label %71

71:                                               ; preds = %101, %66
  %72 = load i64, ptr %11, align 8, !tbaa !15
  %73 = load ptr, ptr @buf, align 8, !tbaa !10
  %74 = call i64 @strlen(ptr noundef %73) #9
  %75 = add i64 %74, 10
  %76 = icmp ult i64 %72, %75
  br i1 %76, label %78, label %77

77:                                               ; preds = %71
  call void @llvm.lifetime.end.p0(i64 8, ptr %11) #9
  br label %104

78:                                               ; preds = %71
  %79 = load i64, ptr %11, align 8, !tbaa !15
  %80 = load i64, ptr %5, align 8, !tbaa !15
  %81 = icmp uge i64 %79, %80
  br i1 %81, label %82, label %89

82:                                               ; preds = %78
  %83 = load i64, ptr %11, align 8, !tbaa !15
  %84 = load i64, ptr %6, align 8, !tbaa !15
  %85 = icmp ule i64 %83, %84
  br i1 %85, label %86, label %89

86:                                               ; preds = %82
  %87 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %88 = call i32 @putc(i32 noundef 94, ptr noundef %87)
  br label %100

89:                                               ; preds = %82, %78
  %90 = load i64, ptr %11, align 8, !tbaa !15
  %91 = load i64, ptr %6, align 8, !tbaa !15
  %92 = icmp ugt i64 %90, %91
  br i1 %92, label %93, label %96

93:                                               ; preds = %89
  %94 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %95 = call i32 @putc(i32 noundef 126, ptr noundef %94)
  br label %99

96:                                               ; preds = %89
  %97 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %98 = call i32 @putc(i32 noundef 32, ptr noundef %97)
  br label %99

99:                                               ; preds = %96, %93
  br label %100

100:                                              ; preds = %99, %86
  br label %101

101:                                              ; preds = %100
  %102 = load i64, ptr %11, align 8, !tbaa !15
  %103 = add i64 %102, 1
  store i64 %103, ptr %11, align 8, !tbaa !15
  br label %71, !llvm.loop !27

104:                                              ; preds = %77
  %105 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %106 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %105, ptr noundef @.str.19) #9
  %107 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %108 = call i32 @putc(i32 noundef 32, ptr noundef %107)
  %109 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %110 = load ptr, ptr %8, align 8, !tbaa !10
  %111 = load ptr, ptr %9, align 8, !tbaa !10
  %112 = call i32 @vfprintf(ptr noundef %109, ptr noundef %110, ptr noundef %111) #9
  %113 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %114 = call i32 @putc(i32 noundef 10, ptr noundef %113)
  %115 = load ptr, ptr @__stderrp, align 8, !tbaa !10
  %116 = call i32 (ptr, ptr, ...) @fprintf(ptr noundef %115, ptr noundef @.str.17) #9
  call void @llvm.va_end.p0(ptr %9)
  call void @llvm.lifetime.end.p0(i64 8, ptr %9) #9
  br label %117

117:                                              ; preds = %104, %14
  ret void
}

; Function Attrs: nounwind
declare i64 @strlen(ptr noundef) #4

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(i64 immarg, ptr nocapture) #2

; Function Attrs: allocsize(1)
declare ptr @realloc(ptr noundef, i64 noundef) #5

; Function Attrs: cold
declare void @perror(ptr noundef) #6

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @parse_expression() #0 {
  %1 = alloca %struct.Token, align 8
  %2 = call signext i8 @advance()
  store i32 -1, ptr @current_token, align 8, !tbaa !25
  call void @llvm.lifetime.start.p0(i64 24, ptr %1) #9
  call void @advance_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %1)
  call void @llvm.lifetime.end.p0(i64 24, ptr %1) #9
  %3 = call i64 @parse_sums()
  ret i64 %3
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal signext i8 @advance() #0 {
  %1 = alloca i8, align 1
  %2 = alloca i8, align 1
  %3 = load ptr, ptr @current, align 8, !tbaa !10
  %4 = icmp ne ptr %3, null
  br i1 %4, label %7, label %5

5:                                                ; preds = %0
  store i64 0, ptr @col_no, align 8, !tbaa !15
  %6 = load ptr, ptr @buf, align 8, !tbaa !10
  store ptr %6, ptr @current, align 8, !tbaa !10
  store i8 0, ptr %1, align 1
  br label %21

7:                                                ; preds = %0
  call void @llvm.lifetime.start.p0(i64 1, ptr %2) #9
  %8 = load ptr, ptr @current, align 8, !tbaa !10
  %9 = load i8, ptr %8, align 1, !tbaa !24
  store i8 %9, ptr %2, align 1, !tbaa !24
  %10 = load ptr, ptr @current, align 8, !tbaa !10
  %11 = load i8, ptr %10, align 1, !tbaa !24
  %12 = sext i8 %11 to i32
  %13 = icmp ne i32 %12, 0
  br i1 %13, label %14, label %19

14:                                               ; preds = %7
  %15 = load ptr, ptr @current, align 8, !tbaa !10
  %16 = getelementptr inbounds i8, ptr %15, i32 1
  store ptr %16, ptr @current, align 8, !tbaa !10
  %17 = load i64, ptr @col_no, align 8, !tbaa !15
  %18 = add i64 %17, 1
  store i64 %18, ptr @col_no, align 8, !tbaa !15
  br label %19

19:                                               ; preds = %14, %7
  %20 = load i8, ptr %2, align 1, !tbaa !24
  store i8 %20, ptr %1, align 1
  call void @llvm.lifetime.end.p0(i64 1, ptr %2) #9
  br label %21

21:                                               ; preds = %19, %5
  %22 = load i8, ptr %1, align 1
  ret i8 %22
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @advance_token(ptr dead_on_unwind noalias writable sret(%struct.Token) align 8 %0) #0 {
  %2 = alloca %struct.Token, align 8
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %0, ptr align 8 @current_token, i64 24, i1 false), !tbaa.struct !28
  %3 = getelementptr inbounds %struct.Token, ptr %0, i32 0, i32 0
  %4 = load i32, ptr %3, align 8, !tbaa !25
  %5 = icmp ne i32 %4, 7
  br i1 %5, label %6, label %7

6:                                                ; preds = %1
  call void @llvm.lifetime.start.p0(i64 24, ptr %2) #9
  call void @next_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %2)
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 @current_token, ptr align 8 %2, i64 24, i1 false), !tbaa.struct !28
  call void @llvm.lifetime.end.p0(i64 24, ptr %2) #9
  br label %7

7:                                                ; preds = %6, %1
  ret void
}

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: readwrite)
declare void @llvm.memcpy.p0.p0.i64(ptr noalias nocapture writeonly, ptr noalias nocapture readonly, i64, i1 immarg) #7

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @next_token(ptr dead_on_unwind noalias writable sret(%struct.Token) align 8 %0) #0 {
  %2 = alloca i8, align 1
  %3 = alloca i32, align 4
  br label %4

4:                                                ; preds = %34, %1
  call void @llvm.lifetime.start.p0(i64 1, ptr %2) #9
  %5 = call signext i8 @peek()
  store i8 %5, ptr %2, align 1, !tbaa !24
  %6 = load i8, ptr %2, align 1, !tbaa !24
  %7 = sext i8 %6 to i32
  %8 = icmp eq i32 %7, 0
  br i1 %8, label %9, label %10

9:                                                ; preds = %4
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 7, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

10:                                               ; preds = %4
  %11 = call signext i8 @advance()
  %12 = load i8, ptr %2, align 1, !tbaa !24
  %13 = sext i8 %12 to i32
  switch i32 %13, label %21 [
    i32 43, label %14
    i32 45, label %15
    i32 42, label %16
    i32 47, label %17
    i32 41, label %18
    i32 40, label %19
    i32 32, label %20
    i32 9, label %20
    i32 10, label %20
    i32 13, label %20
  ]

14:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 0, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

15:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 1, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

16:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 2, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

17:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 3, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

18:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 5, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

19:                                               ; preds = %10
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 4, i64 noundef 0)
  store i32 1, ptr %3, align 4
  br label %34

20:                                               ; preds = %10, %10, %10, %10
  store i32 3, ptr %3, align 4
  br label %34, !llvm.loop !29

21:                                               ; preds = %10
  %22 = load i8, ptr %2, align 1, !tbaa !24
  %23 = call zeroext i1 @is_number(i8 noundef signext %22)
  br i1 %23, label %24, label %27

24:                                               ; preds = %21
  %25 = load i8, ptr %2, align 1, !tbaa !24
  %26 = call i64 @number(i8 noundef signext %25)
  call void @create_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %0, i32 noundef 6, i64 noundef %26)
  store i32 1, ptr %3, align 4
  br label %34

27:                                               ; preds = %21
  %28 = load i64, ptr @col_no, align 8, !tbaa !15
  %29 = sub i64 %28, 1
  %30 = load i64, ptr @col_no, align 8, !tbaa !15
  %31 = sub i64 %30, 1
  %32 = load i8, ptr %2, align 1, !tbaa !24
  %33 = sext i8 %32 to i32
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %29, i64 noundef %31, ptr noundef @.str.6, ptr noundef @.str.7, i32 noundef %33)
  store i32 3, ptr %3, align 4
  br label %34, !llvm.loop !29

34:                                               ; preds = %27, %24, %20, %19, %18, %17, %16, %15, %14, %9
  call void @llvm.lifetime.end.p0(i64 1, ptr %2) #9
  %35 = load i32, ptr %3, align 4
  switch i32 %35, label %37 [
    i32 1, label %36
    i32 3, label %4
  ]

36:                                               ; preds = %34
  ret void

37:                                               ; preds = %34
  unreachable
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @create_token(ptr dead_on_unwind noalias writable sret(%struct.Token) align 8 %0, i32 noundef %1, i64 noundef %2) #0 {
  %4 = alloca i32, align 4
  %5 = alloca i64, align 8
  store i32 %1, ptr %4, align 4, !tbaa !6
  store i64 %2, ptr %5, align 8, !tbaa !15
  %6 = getelementptr inbounds %struct.Token, ptr %0, i32 0, i32 0
  %7 = load i32, ptr %4, align 4, !tbaa !6
  store i32 %7, ptr %6, align 8, !tbaa !25
  %8 = getelementptr inbounds %struct.Token, ptr %0, i32 0, i32 1
  %9 = load i64, ptr %5, align 8, !tbaa !15
  store i64 %9, ptr %8, align 8, !tbaa !30
  %10 = getelementptr inbounds %struct.Token, ptr %0, i32 0, i32 2
  %11 = load i64, ptr @col_no, align 8, !tbaa !15
  %12 = sub i64 %11, 1
  store i64 %12, ptr %10, align 8, !tbaa !17
  ret void
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal zeroext i1 @is_number(i8 noundef signext %0) #0 {
  %2 = alloca i8, align 1
  store i8 %0, ptr %2, align 1, !tbaa !24
  %3 = load i8, ptr %2, align 1, !tbaa !24
  %4 = sext i8 %3 to i32
  %5 = icmp sle i32 48, %4
  br i1 %5, label %6, label %10

6:                                                ; preds = %1
  %7 = load i8, ptr %2, align 1, !tbaa !24
  %8 = sext i8 %7 to i32
  %9 = icmp sle i32 %8, 57
  br label %10

10:                                               ; preds = %6, %1
  %11 = phi i1 [ false, %1 ], [ %9, %6 ]
  ret i1 %11
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @number(i8 noundef signext %0) #0 {
  %2 = alloca i8, align 1
  %3 = alloca i64, align 8
  store i8 %0, ptr %2, align 1, !tbaa !24
  call void @llvm.lifetime.start.p0(i64 8, ptr %3) #9
  %4 = load i8, ptr %2, align 1, !tbaa !24
  %5 = sext i8 %4 to i32
  %6 = sub nsw i32 %5, 48
  %7 = sext i32 %6 to i64
  store i64 %7, ptr %3, align 8, !tbaa !15
  br label %8

8:                                                ; preds = %11, %1
  %9 = call signext i8 @peek()
  %10 = call zeroext i1 @is_number(i8 noundef signext %9)
  br i1 %10, label %11, label %20

11:                                               ; preds = %8
  %12 = load i64, ptr %3, align 8, !tbaa !15
  %13 = mul nsw i64 %12, 10
  store i64 %13, ptr %3, align 8, !tbaa !15
  %14 = call signext i8 @advance()
  %15 = sext i8 %14 to i32
  %16 = sub nsw i32 %15, 48
  %17 = sext i32 %16 to i64
  %18 = load i64, ptr %3, align 8, !tbaa !15
  %19 = add nsw i64 %18, %17
  store i64 %19, ptr %3, align 8, !tbaa !15
  br label %8, !llvm.loop !31

20:                                               ; preds = %8
  %21 = load i64, ptr %3, align 8, !tbaa !15
  call void @llvm.lifetime.end.p0(i64 8, ptr %3) #9
  ret i64 %21
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal signext i8 @peek() #0 {
  %1 = load ptr, ptr @current, align 8, !tbaa !10
  %2 = load i8, ptr %1, align 1, !tbaa !24
  ret i8 %2
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @parse_sums() #0 {
  %1 = alloca i64, align 8
  call void @llvm.lifetime.start.p0(i64 8, ptr %1) #9
  %2 = call i64 @parse_products()
  store i64 %2, ptr %1, align 8, !tbaa !15
  br label %3

3:                                                ; preds = %18, %0
  br label %4

4:                                                ; preds = %3
  %5 = call zeroext i1 @match_token(i32 noundef 0)
  br i1 %5, label %6, label %10

6:                                                ; preds = %4
  %7 = call i64 @parse_products()
  %8 = load i64, ptr %1, align 8, !tbaa !15
  %9 = add nsw i64 %8, %7
  store i64 %9, ptr %1, align 8, !tbaa !15
  br label %18

10:                                               ; preds = %4
  %11 = call zeroext i1 @match_token(i32 noundef 1)
  br i1 %11, label %12, label %16

12:                                               ; preds = %10
  %13 = call i64 @parse_products()
  %14 = load i64, ptr %1, align 8, !tbaa !15
  %15 = sub nsw i64 %14, %13
  store i64 %15, ptr %1, align 8, !tbaa !15
  br label %17

16:                                               ; preds = %10
  br label %19

17:                                               ; preds = %12
  br label %18

18:                                               ; preds = %17, %6
  br label %3, !llvm.loop !32

19:                                               ; preds = %16
  %20 = load i64, ptr %1, align 8, !tbaa !15
  call void @llvm.lifetime.end.p0(i64 8, ptr %1) #9
  ret i64 %20
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @parse_products() #0 {
  %1 = alloca i64, align 8
  %2 = alloca i64, align 8
  %3 = alloca %struct.Token, align 8
  %4 = alloca i64, align 8
  %5 = alloca %struct.Token, align 8
  %6 = alloca i32, align 4
  call void @llvm.lifetime.start.p0(i64 8, ptr %2) #9
  %7 = call i64 @parse_unary()
  store i64 %7, ptr %2, align 8, !tbaa !15
  br label %8

8:                                                ; preds = %35, %0
  br label %9

9:                                                ; preds = %8
  %10 = call zeroext i1 @match_token(i32 noundef 2)
  br i1 %10, label %11, label %15

11:                                               ; preds = %9
  %12 = call i64 @parse_unary()
  %13 = load i64, ptr %2, align 8, !tbaa !15
  %14 = mul nsw i64 %13, %12
  store i64 %14, ptr %2, align 8, !tbaa !15
  br label %35

15:                                               ; preds = %9
  %16 = call zeroext i1 @match_token(i32 noundef 3)
  br i1 %16, label %17, label %33

17:                                               ; preds = %15
  call void @llvm.lifetime.start.p0(i64 24, ptr %3) #9
  call void @peek_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %3)
  call void @llvm.lifetime.start.p0(i64 8, ptr %4) #9
  %18 = call i64 @parse_unary()
  store i64 %18, ptr %4, align 8, !tbaa !15
  call void @llvm.lifetime.start.p0(i64 24, ptr %5) #9
  call void @peek_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %5)
  %19 = load i64, ptr %4, align 8, !tbaa !15
  %20 = icmp eq i64 %19, 0
  br i1 %20, label %21, label %26

21:                                               ; preds = %17
  %22 = getelementptr inbounds %struct.Token, ptr %3, i32 0, i32 2
  %23 = load i64, ptr %22, align 8, !tbaa !17
  %24 = getelementptr inbounds %struct.Token, ptr %5, i32 0, i32 2
  %25 = load i64, ptr %24, align 8, !tbaa !17
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %23, i64 noundef %25, ptr noundef @.str.8, ptr noundef @.str.9)
  store i64 0, ptr %1, align 8
  store i32 1, ptr %6, align 4
  br label %30

26:                                               ; preds = %17
  %27 = load i64, ptr %4, align 8, !tbaa !15
  %28 = load i64, ptr %2, align 8, !tbaa !15
  %29 = sdiv i64 %28, %27
  store i64 %29, ptr %2, align 8, !tbaa !15
  store i32 0, ptr %6, align 4
  br label %30

30:                                               ; preds = %26, %21
  call void @llvm.lifetime.end.p0(i64 24, ptr %5) #9
  call void @llvm.lifetime.end.p0(i64 8, ptr %4) #9
  call void @llvm.lifetime.end.p0(i64 24, ptr %3) #9
  %31 = load i32, ptr %6, align 4
  switch i32 %31, label %38 [
    i32 0, label %32
  ]

32:                                               ; preds = %30
  br label %34

33:                                               ; preds = %15
  br label %36

34:                                               ; preds = %32
  br label %35

35:                                               ; preds = %34, %11
  br label %8, !llvm.loop !33

36:                                               ; preds = %33
  %37 = load i64, ptr %2, align 8, !tbaa !15
  store i64 %37, ptr %1, align 8
  store i32 1, ptr %6, align 4
  br label %38

38:                                               ; preds = %36, %30
  call void @llvm.lifetime.end.p0(i64 8, ptr %2) #9
  %39 = load i64, ptr %1, align 8
  ret i64 %39
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @parse_unary() #0 {
  %1 = call zeroext i1 @match_token(i32 noundef 1)
  br i1 %1, label %2, label %5

2:                                                ; preds = %0
  %3 = call i64 @parse_unary()
  %4 = sub nsw i64 0, %3
  br label %7

5:                                                ; preds = %0
  %6 = call i64 @parse_primary()
  br label %7

7:                                                ; preds = %5, %2
  %8 = phi i64 [ %4, %2 ], [ %6, %5 ]
  ret i64 %8
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal i64 @parse_primary() #0 {
  %1 = alloca i64, align 8
  %2 = alloca %struct.Token, align 8
  %3 = alloca i64, align 8
  %4 = alloca i64, align 8
  %5 = alloca %struct.Token, align 8
  %6 = alloca i32, align 4
  call void @llvm.lifetime.start.p0(i64 24, ptr %2) #9
  call void @peek_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %2)
  %7 = call zeroext i1 @match_token(i32 noundef 4)
  br i1 %7, label %8, label %20

8:                                                ; preds = %0
  call void @llvm.lifetime.start.p0(i64 8, ptr %3) #9
  %9 = call i64 @parse_sums()
  store i64 %9, ptr %3, align 8, !tbaa !15
  call void @llvm.lifetime.start.p0(i64 8, ptr %4) #9
  call void @peek_token(ptr dead_on_unwind writable sret(%struct.Token) align 8 %5)
  %10 = getelementptr inbounds %struct.Token, ptr %5, i32 0, i32 2
  %11 = load i64, ptr %10, align 8, !tbaa !17
  store i64 %11, ptr %4, align 8, !tbaa !15
  %12 = call zeroext i1 @match_token(i32 noundef 5)
  br i1 %12, label %18, label %13

13:                                               ; preds = %8
  %14 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %15 = load i64, ptr %14, align 8, !tbaa !17
  %16 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %17 = load i64, ptr %16, align 8, !tbaa !17
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %15, i64 noundef %17, ptr noundef @.str.10, ptr noundef @.str.11)
  br label %18

18:                                               ; preds = %13, %8
  %19 = load i64, ptr %3, align 8, !tbaa !15
  store i64 %19, ptr %1, align 8
  store i32 1, ptr %6, align 4
  call void @llvm.lifetime.end.p0(i64 8, ptr %4) #9
  call void @llvm.lifetime.end.p0(i64 8, ptr %3) #9
  br label %37

20:                                               ; preds = %0
  %21 = call zeroext i1 @match_token(i32 noundef 6)
  br i1 %21, label %22, label %25

22:                                               ; preds = %20
  %23 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 1
  %24 = load i64, ptr %23, align 8, !tbaa !30
  store i64 %24, ptr %1, align 8
  store i32 1, ptr %6, align 4
  br label %37

25:                                               ; preds = %20
  %26 = call zeroext i1 @match_token(i32 noundef 7)
  br i1 %26, label %27, label %32

27:                                               ; preds = %25
  %28 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %29 = load i64, ptr %28, align 8, !tbaa !17
  %30 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %31 = load i64, ptr %30, align 8, !tbaa !17
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %29, i64 noundef %31, ptr noundef @.str.12, ptr noundef @.str.13)
  store i64 0, ptr %1, align 8
  store i32 1, ptr %6, align 4
  br label %37

32:                                               ; preds = %25
  %33 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %34 = load i64, ptr %33, align 8, !tbaa !17
  %35 = getelementptr inbounds %struct.Token, ptr %2, i32 0, i32 2
  %36 = load i64, ptr %35, align 8, !tbaa !17
  call void (i64, i64, ptr, ptr, ...) @error(i64 noundef %34, i64 noundef %36, ptr noundef @.str.14, ptr noundef @.str.15)
  store i64 0, ptr %1, align 8
  store i32 1, ptr %6, align 4
  br label %37

37:                                               ; preds = %32, %27, %22, %18
  call void @llvm.lifetime.end.p0(i64 24, ptr %2) #9
  %38 = load i64, ptr %1, align 8
  ret i64 %38
}

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare void @llvm.va_start.p0(ptr) #8

; Function Attrs: nounwind
declare i32 @fprintf(ptr noundef, ptr noundef, ...) #4

; Function Attrs: nounwind
declare i32 @vfprintf(ptr noundef, ptr noundef, ptr noundef) #4

declare i32 @putc(i32 noundef, ptr noundef) #1

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare void @llvm.va_end.p0(ptr) #8

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @peek_token(ptr dead_on_unwind noalias writable sret(%struct.Token) align 8 %0) #0 {
  call void @llvm.memcpy.p0.p0.i64(ptr align 8 %0, ptr align 8 @current_token, i64 24, i1 false), !tbaa.struct !28
  ret void
}

; Function Attrs: nounwind ssp uwtable(sync)
define internal void @buffer_reset() #0 {
  store i64 0, ptr @buf_count, align 8, !tbaa !15
  store i64 0, ptr @buf_size, align 8, !tbaa !15
  store ptr null, ptr @current, align 8, !tbaa !10
  %1 = load ptr, ptr @buf, align 8, !tbaa !10
  %2 = icmp ne ptr %1, null
  br i1 %2, label %3, label %5

3:                                                ; preds = %0
  %4 = load ptr, ptr @buf, align 8, !tbaa !10
  call void @free(ptr noundef %4)
  store ptr null, ptr @buf, align 8, !tbaa !10
  br label %5

5:                                                ; preds = %3, %0
  ret void
}

declare void @free(ptr noundef) #1

attributes #0 = { nounwind ssp uwtable(sync) "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #1 = { "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #2 = { nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #3 = { noreturn "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #4 = { nounwind "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #5 = { allocsize(1) "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #6 = { cold "frame-pointer"="non-leaf" "no-trapping-math"="true" "probe-stack"="__chkstk_darwin" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+bti,+ccdp,+ccidx,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8.5a,+v8a,+zcm,+zcz" }
attributes #7 = { nocallback nofree nounwind willreturn memory(argmem: readwrite) }
attributes #8 = { nocallback nofree nosync nounwind willreturn }
attributes #9 = { nounwind }
attributes #10 = { noreturn }
attributes #11 = { allocsize(1) }
attributes #12 = { cold }

!llvm.module.flags = !{!0, !1, !2, !3, !4}
!llvm.ident = !{!5}

!0 = !{i32 2, !"SDK Version", [2 x i32] [i32 15, i32 5]}
!1 = !{i32 1, !"wchar_size", i32 4}
!2 = !{i32 8, !"PIC Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 1}
!4 = !{i32 7, !"frame-pointer", i32 1}
!5 = !{!"Apple clang version 17.0.0 (clang-1700.0.13.5)"}
!6 = !{!7, !7, i64 0}
!7 = !{!"int", !8, i64 0}
!8 = !{!"omnipotent char", !9, i64 0}
!9 = !{!"Simple C/C++ TBAA"}
!10 = !{!11, !11, i64 0}
!11 = !{!"any pointer", !8, i64 0}
!12 = distinct !{!12, !13, !14}
!13 = !{!"llvm.loop.mustprogress"}
!14 = !{!"llvm.loop.unroll.disable"}
!15 = !{!16, !16, i64 0}
!16 = !{!"long", !8, i64 0}
!17 = !{!18, !16, i64 16}
!18 = !{!"", !7, i64 0, !16, i64 8, !16, i64 16}
!19 = !{!20, !20, i64 0}
!20 = !{!"_Bool", !8, i64 0}
!21 = !{i8 0, i8 2}
!22 = !{}
!23 = distinct !{!23, !14}
!24 = !{!8, !8, i64 0}
!25 = !{!18, !7, i64 0}
!26 = distinct !{!26, !13, !14}
!27 = distinct !{!27, !13, !14}
!28 = !{i64 0, i64 4, !6, i64 8, i64 8, !15, i64 16, i64 8, !15}
!29 = distinct !{!29, !14}
!30 = !{!18, !16, i64 8}
!31 = distinct !{!31, !13, !14}
!32 = distinct !{!32, !14}
!33 = distinct !{!33, !14}
