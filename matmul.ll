; ModuleID = 'matmul.c'
source_filename = "matmul.c"
target datalayout = "e-m:o-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-n32:64-S128-Fn32"
target triple = "arm64-apple-macosx26.0.0"

%struct.ident_t = type { i32, i32, i32, i32, ptr }

@0 = private unnamed_addr constant [23 x i8] c";unknown;unknown;0;0;;\00", align 1
@1 = private unnamed_addr constant %struct.ident_t { i32 0, i32 514, i32 0, i32 22, ptr @0 }, align 8
@2 = private unnamed_addr constant %struct.ident_t { i32 0, i32 2, i32 0, i32 22, ptr @0 }, align 8

; Function Attrs: noinline nounwind optnone ssp uwtable(sync)
define i32 @main(i32 noundef %0, ptr noundef %1) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca ptr, align 8
  %6 = alloca [128 x [128 x double]], align 8
  %7 = alloca [128 x [128 x double]], align 8
  %8 = alloca [128 x [128 x double]], align 8
  %9 = alloca i32, align 4
  %10 = alloca i32, align 4
  store i32 0, ptr %3, align 4
  store i32 %0, ptr %4, align 4
  store ptr %1, ptr %5, align 8
  %11 = call i64 @time(ptr noundef null)
  %12 = trunc i64 %11 to i32
  call void @srand(i32 noundef %12)
  store i32 0, ptr %9, align 4
  br label %13

13:                                               ; preds = %43, %2
  %14 = load i32, ptr %9, align 4
  %15 = icmp slt i32 %14, 128
  br i1 %15, label %16, label %46

16:                                               ; preds = %13
  store i32 0, ptr %10, align 4
  br label %17

17:                                               ; preds = %39, %16
  %18 = load i32, ptr %10, align 4
  %19 = icmp slt i32 %18, 128
  br i1 %19, label %20, label %42

20:                                               ; preds = %17
  %21 = call i32 @rand()
  %22 = sitofp i32 %21 to double
  %23 = fdiv double %22, 0x41DFFFFFFFC00000
  %24 = load i32, ptr %9, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds [128 x [128 x double]], ptr %6, i64 0, i64 %25
  %27 = load i32, ptr %10, align 4
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds [128 x double], ptr %26, i64 0, i64 %28
  store double %23, ptr %29, align 8
  %30 = call i32 @rand()
  %31 = sitofp i32 %30 to double
  %32 = fdiv double %31, 0x41DFFFFFFFC00000
  %33 = load i32, ptr %9, align 4
  %34 = sext i32 %33 to i64
  %35 = getelementptr inbounds [128 x [128 x double]], ptr %7, i64 0, i64 %34
  %36 = load i32, ptr %10, align 4
  %37 = sext i32 %36 to i64
  %38 = getelementptr inbounds [128 x double], ptr %35, i64 0, i64 %37
  store double %32, ptr %38, align 8
  br label %39

39:                                               ; preds = %20
  %40 = load i32, ptr %10, align 4
  %41 = add nsw i32 %40, 1
  store i32 %41, ptr %10, align 4
  br label %17, !llvm.loop !7

42:                                               ; preds = %17
  br label %43

43:                                               ; preds = %42
  %44 = load i32, ptr %9, align 4
  %45 = add nsw i32 %44, 1
  store i32 %45, ptr %9, align 4
  br label %13, !llvm.loop !9

46:                                               ; preds = %13
  call void (ptr, i32, ptr, ...) @__kmpc_fork_call(ptr @2, i32 3, ptr @main.omp_outlined, ptr %8, ptr %6, ptr %7)
  %47 = load i32, ptr %3, align 4
  ret i32 %47
}

declare void @srand(i32 noundef) #1

declare i64 @time(ptr noundef) #1

declare i32 @rand() #1

; Function Attrs: noinline norecurse nounwind optnone ssp uwtable(sync)
define internal void @main.omp_outlined(ptr noalias noundef %0, ptr noalias noundef %1, ptr noundef nonnull align 8 dereferenceable(131072) %2, ptr noundef nonnull align 8 dereferenceable(131072) %3, ptr noundef nonnull align 8 dereferenceable(131072) %4) #2 {
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  %9 = alloca ptr, align 8
  %10 = alloca ptr, align 8
  %11 = alloca i32, align 4
  %12 = alloca i32, align 4
  %13 = alloca i32, align 4
  %14 = alloca i32, align 4
  %15 = alloca i32, align 4
  %16 = alloca i32, align 4
  %17 = alloca i32, align 4
  %18 = alloca i32, align 4
  %19 = alloca i32, align 4
  store ptr %0, ptr %6, align 8
  store ptr %1, ptr %7, align 8
  store ptr %2, ptr %8, align 8
  store ptr %3, ptr %9, align 8
  store ptr %4, ptr %10, align 8
  %20 = load ptr, ptr %8, align 8, !nonnull !10, !align !11
  %21 = load ptr, ptr %9, align 8, !nonnull !10, !align !11
  %22 = load ptr, ptr %10, align 8, !nonnull !10, !align !11
  store i32 0, ptr %13, align 4
  store i32 127, ptr %14, align 4
  store i32 1, ptr %15, align 4
  store i32 0, ptr %16, align 4
  %23 = load ptr, ptr %6, align 8
  %24 = load i32, ptr %23, align 4
  call void @__kmpc_for_static_init_4(ptr @1, i32 %24, i32 34, ptr %16, ptr %13, ptr %14, ptr %15, i32 1, i32 1)
  %25 = load i32, ptr %14, align 4
  %26 = icmp sgt i32 %25, 127
  br i1 %26, label %27, label %28

27:                                               ; preds = %5
  br label %30

28:                                               ; preds = %5
  %29 = load i32, ptr %14, align 4
  br label %30

30:                                               ; preds = %28, %27
  %31 = phi i32 [ 127, %27 ], [ %29, %28 ]
  store i32 %31, ptr %14, align 4
  %32 = load i32, ptr %13, align 4
  store i32 %32, ptr %11, align 4
  br label %33

33:                                               ; preds = %80, %30
  %34 = load i32, ptr %11, align 4
  %35 = load i32, ptr %14, align 4
  %36 = icmp sle i32 %34, %35
  br i1 %36, label %37, label %83

37:                                               ; preds = %33
  %38 = load i32, ptr %11, align 4
  %39 = mul nsw i32 %38, 1
  %40 = add nsw i32 0, %39
  store i32 %40, ptr %17, align 4
  store i32 0, ptr %18, align 4
  br label %41

41:                                               ; preds = %75, %37
  %42 = load i32, ptr %18, align 4
  %43 = icmp slt i32 %42, 128
  br i1 %43, label %44, label %78

44:                                               ; preds = %41
  store i32 0, ptr %19, align 4
  br label %45

45:                                               ; preds = %71, %44
  %46 = load i32, ptr %19, align 4
  %47 = icmp slt i32 %46, 128
  br i1 %47, label %48, label %74

48:                                               ; preds = %45
  %49 = load i32, ptr %17, align 4
  %50 = sext i32 %49 to i64
  %51 = getelementptr inbounds [128 x [128 x double]], ptr %21, i64 0, i64 %50
  %52 = load i32, ptr %18, align 4
  %53 = sext i32 %52 to i64
  %54 = getelementptr inbounds [128 x double], ptr %51, i64 0, i64 %53
  %55 = load double, ptr %54, align 8
  %56 = load i32, ptr %18, align 4
  %57 = sext i32 %56 to i64
  %58 = getelementptr inbounds [128 x [128 x double]], ptr %22, i64 0, i64 %57
  %59 = load i32, ptr %19, align 4
  %60 = sext i32 %59 to i64
  %61 = getelementptr inbounds [128 x double], ptr %58, i64 0, i64 %60
  %62 = load double, ptr %61, align 8
  %63 = load i32, ptr %17, align 4
  %64 = sext i32 %63 to i64
  %65 = getelementptr inbounds [128 x [128 x double]], ptr %20, i64 0, i64 %64
  %66 = load i32, ptr %19, align 4
  %67 = sext i32 %66 to i64
  %68 = getelementptr inbounds [128 x double], ptr %65, i64 0, i64 %67
  %69 = load double, ptr %68, align 8
  %70 = call double @llvm.fmuladd.f64(double %55, double %62, double %69)
  store double %70, ptr %68, align 8
  br label %71

71:                                               ; preds = %48
  %72 = load i32, ptr %19, align 4
  %73 = add nsw i32 %72, 1
  store i32 %73, ptr %19, align 4
  br label %45, !llvm.loop !12

74:                                               ; preds = %45
  br label %75

75:                                               ; preds = %74
  %76 = load i32, ptr %18, align 4
  %77 = add nsw i32 %76, 1
  store i32 %77, ptr %18, align 4
  br label %41, !llvm.loop !13

78:                                               ; preds = %41
  br label %79

79:                                               ; preds = %78
  br label %80

80:                                               ; preds = %79
  %81 = load i32, ptr %11, align 4
  %82 = add nsw i32 %81, 1
  store i32 %82, ptr %11, align 4
  br label %33

83:                                               ; preds = %33
  br label %84

84:                                               ; preds = %83
  call void @__kmpc_for_static_fini(ptr @1, i32 %24)
  ret void
}

; Function Attrs: nounwind
declare void @__kmpc_for_static_init_4(ptr, i32, i32, ptr, ptr, ptr, ptr, i32, i32) #3

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.fmuladd.f64(double, double, double) #4

; Function Attrs: nounwind
declare void @__kmpc_for_static_fini(ptr, i32) #3

; Function Attrs: nounwind
declare !callback !14 void @__kmpc_fork_call(ptr, i32, ptr, ...) #3

attributes #0 = { noinline nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf-no-reserve" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+ccdp,+ccidx,+ccpp,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8a" }
attributes #1 = { "frame-pointer"="non-leaf-no-reserve" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+ccdp,+ccidx,+ccpp,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8a" }
attributes #2 = { noinline norecurse nounwind optnone ssp uwtable(sync) "frame-pointer"="non-leaf-no-reserve" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="apple-m1" "target-features"="+aes,+altnzcv,+ccdp,+ccidx,+ccpp,+complxnum,+crc,+dit,+dotprod,+flagm,+fp-armv8,+fp16fml,+fptoint,+fullfp16,+jsconv,+lse,+neon,+pauth,+perfmon,+predres,+ras,+rcpc,+rdm,+sb,+sha2,+sha3,+specrestrict,+ssbs,+v8.1a,+v8.2a,+v8.3a,+v8.4a,+v8a" }
attributes #3 = { nounwind }
attributes #4 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }

!llvm.module.flags = !{!0, !1, !2, !3, !4, !5}
!llvm.ident = !{!6}

!0 = !{i32 2, !"SDK Version", [2 x i32] [i32 26, i32 5]}
!1 = !{i32 1, !"wchar_size", i32 4}
!2 = !{i32 7, !"openmp", i32 51}
!3 = !{i32 8, !"PIC Level", i32 2}
!4 = !{i32 7, !"uwtable", i32 1}
!5 = !{i32 7, !"frame-pointer", i32 4}
!6 = !{!"Homebrew clang version 22.1.5"}
!7 = distinct !{!7, !8}
!8 = !{!"llvm.loop.mustprogress"}
!9 = distinct !{!9, !8}
!10 = !{}
!11 = !{i64 8}
!12 = distinct !{!12, !8}
!13 = distinct !{!13, !8}
!14 = !{!15}
!15 = !{i64 2, i64 -1, i64 -1, i1 true}
