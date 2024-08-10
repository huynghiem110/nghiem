#ifndef PLATFORM_TYPES_H
#define PLATFORM_TYPES_H

#include <stdbool.h>
#include <stdint.h>

#define TRUE true
#define FALSE false

#define PLATFORM_VENDOR_ID 0x0006u
#define PLATFORM_MODULE_ID 0x00C7u

#define CPU_TYPE_8 8
#define CPU_TYPE_16 16
#define CPU_TYPE_32 32

#define MSB_FIRST 0
#define LSB_FIRST 1

#define HIGH_BYTE_FIRST 0
#define LOW_BYTE_FIRST 1

#define CPU_BIT_ORDER LSB_FIRST
#define CPU_TYPE CPU_TYPE_32
#define CPU_TYPE_ORDER LOW_BYTE_FIRST

typedef int8_t sint8;
typedef uint8_t uint8;
typedef int16_t sint16;
typedef uint16_t uint16;
typedef int32_t sint32;
typedef int64_t sint64;
typedef uint32_t uint32;
typedef uint64_t uint64;

typedef float float32;
typedef double float64;

typedef bool boolean;
typedef int_fast8_t sint8_least;
typedef uint_fast8_t uint8_least;
typedef int_fast16_t sint16_least;
typedef uint_fast16_t uint16_least;
typedef int_fast32_t sint32_least;
typedef uint_fast32_t uint32_least;

#endif










