/*
 * lcd_trans.h
 *
 *  Created on: Nov 4, 2022
 *      Author: Konrad
 */

#ifndef INC_LCD_TRANS_H_
#define INC_LCD_TRANS_H_


#include <stdbool.h>

void lcd_transfer_done(void);
bool lcd_is_busy(void);

#endif /* INC_LCD_TRANS_H_ */
