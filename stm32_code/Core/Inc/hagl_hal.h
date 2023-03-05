/*
 * hagl_hal.h
 *
 *  Created on: Nov 4, 2022
 *      Author: Konrad
 */

#ifndef HAGL_HAL_H_
#define HAGL_HAL_H_

#pragma once

#include "lcd.h"
#include "bitmap.h"

#define DISPLAY_WIDTH 	(LCD_WIDTH)
#define DISPLAY_HEIGHT 	(LCD_HEIGHT)
#define DISPLAY_DEPTH 	16

typedef uint16_t color_t;

#define hagl_hal_put_pixel lcd_put_pixel
#endif /* HAGL_HAL_H_ */
