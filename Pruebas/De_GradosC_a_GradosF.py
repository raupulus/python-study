#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
# Conversor de grados Centígrados a grados F.
# ==============================================================================

gradosC = raw_input('Introduce los grados centígrados --> ')
gradosF = (float(gradosC) * 9 / 5) + 32

print('Equivale a %sºF (grados Fahrenheit)' % gradosF)
