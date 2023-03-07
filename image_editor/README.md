# Как установить и запустить

1. Клонируем репозиторий
2. Устанавливаем poetry командой `pip install poetry`
3. Устанавливаем зависимости командой `poetry install` для первичной установки или `poetry update` для обновления
4. Открываем папку проекта в комнадной строке
5. Чтобы узнать список доступных команд (фильтров), введите команду `poetry run py -m filters_opencv -h`
6. Чтобы узнать аргументы команды (фильтра), введите команду `poetry run py -m filters_opencv <команда (фильтр)> -h`
7. Чтобы выполнить команду (применить фильтр), введите команду `poetry run py -m filters_opencv <команда (фильтр)> <путь к изображению> <путь куда сохранить> <аргументы>`
P.s. В некоторых системам вместо py требуется писать python.

# Список фильтров

* [**Точечные фильтры**](https://github.com/UNNSE21/computer-graphics/tree/Namxobick's-version/image_editor/filters_opencv/filters/point_filters)

1. [Зеркальное отражение](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/geometric_filters/mirror_image.py)
2. [Перенос](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/geometric_filters/relocation.py)
3. [Поворот](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/geometric_filters/rotation.py)
4. [Изменение размера](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/geometric_filters/scale.py)
5. [Изменение яркости](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/changing_brightness.py)
6. [Эффект "стекла"](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/glass_effect.py)
7. [Изоображение в оттенках серого](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/gray_scale.py)
8. [Инверсия](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/inversion.py)
9. [Сепия](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/sepia.py)
10. [Волны](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/point_filters/waves.py)

* [**Локальные фильтры**](https://github.com/UNNSE21/computer-graphics/tree/Namxobick's-version/image_editor/filters_opencv/filters/local_filters)

11. [Размытие](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/blur/arithmetic_mean/blur_by_andrey.py)
12. [Размытие по Гауссу](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/blur/gaussian_blur.py)
13. [Размытие движения](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/blur/motion_blur.py)
14. [Выделение границ по Прюитту](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/border_selection/pruitt.py)
15. [Выделение границ по Щарру](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/border_selection/sharra.py)
16. [Выделение границ по Собелю](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/border_selection/sobel.py)
17. [Наращивание](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/dilation.py)
18. [Эрозия](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/erosion.py)
19. [Размыкание](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/opening.py)
20. [Замыкание](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/closing.py)
21. ["Чёрная шляпа"](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/black_hat.py)
22. ["Верх шляпы"](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/top_hat.py)
23. [Grad](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/mathematical_morphology/grad.py)
24. [Тиснение](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/embossing.py)
25. [Светящиеся края](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/glowing_edges.py)
26. [Повышение резкости](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/increase_sharpness.py)
27. [Фильтр максимума](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/maximum.py)
28. [Медианный фильтр](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/local_filters/median.py)

* [**Глобальные фильтры**](https://github.com/UNNSE21/computer-graphics/tree/Namxobick's-version/image_editor/filters_opencv/filters/global_filters)
29. [Усреднение яркости](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/medium_filters/averaging_color.py)
30. [Затемнение](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/medium_filters/darkening.py)
31. ["Серый мир"](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/medium_filters/gray_world.py)
32. [Осветление](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/medium_filters/lightening.py)
33. [Коррекция "autolevels"](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/autolevels.py)
34. [Коррекция с опорным цветом](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/correction_with_reference_color.py)
35. [Линейное растяжение](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/linear_stretching.py)
36. [Идеальный отражатель](https://github.com/UNNSE21/computer-graphics/blob/Namxobick's-version/image_editor/filters_opencv/filters/global_filters/perfect_reflector.py)

# Примеры (До / После)

## Зеркальное отражение
![зеркальное_отражение](https://user-images.githubusercontent.com/100288192/222975746-2f084fc4-3311-49de-8b80-0a137e1b0169.png)
## Перенос
![перенос](https://user-images.githubusercontent.com/100288192/222976795-1167a9d6-a1b7-4075-8f08-f063a9d01973.png)
## Поворот
![поворот](https://user-images.githubusercontent.com/100288192/222976807-649a7e88-731e-4803-aadc-5beafd1d2a10.png)
## Изменение размера
![изменение_размера](https://user-images.githubusercontent.com/100288192/222976852-d19f9fb2-7a71-424c-8790-e35f05327f15.png)
## Эффект "стекла"
![эффект_стекла](https://user-images.githubusercontent.com/100288192/222976865-e0350656-1a7e-41d9-8aca-265d3bd1b30b.png)
## Изоображение в оттенках серого
![оттенки_серого](https://user-images.githubusercontent.com/100288192/222976888-987d02be-98d2-41e5-b1b8-69ee07eeae28.png)
## Инверсия
![инверсия](https://user-images.githubusercontent.com/100288192/222976902-9d351f7a-5b7a-4bed-96fd-b7ce99406e97.png)
## Сепия
![сепия](https://user-images.githubusercontent.com/100288192/222976944-6dadbc6f-1d53-4803-a802-3f051b5251e7.png)
## Волны
![волны](https://user-images.githubusercontent.com/100288192/222976951-70df904f-185e-4e1b-bef9-817ff042d29f.png)
## Размытие
![blur_2x2](https://user-images.githubusercontent.com/100288192/223200404-cffadc70-254d-409c-b39c-97fcad40d13a.png)
## Размытие по Гауссу
![blur_gaussian_sigma=2,1](https://user-images.githubusercontent.com/100288192/223200458-2154e7b7-ae68-43a3-b6af-bf16ab47d94f.png)
## Размытие движения
![motion_blur](https://user-images.githubusercontent.com/100288192/223200519-815bf98d-8a4d-49dd-bb59-65f1302606df.png)
## Выделение границ по Прюитту
![pruitt](https://user-images.githubusercontent.com/100288192/223200588-c3ea2f1d-51e1-4b77-afc4-1a172b14cb34.png)
## Выделение границ по Щарру
![sharra](https://user-images.githubusercontent.com/100288192/223200628-6dff7bfb-528c-48af-9cb7-124a6a019ee8.png)
## Выделение границ по Собелю
![sobel](https://user-images.githubusercontent.com/100288192/223200653-ecb0eaad-2f68-407b-b395-9cd0dee85cac.png)
## Наращивание
![dilation](https://user-images.githubusercontent.com/100288192/223203230-031fdbed-380d-4e29-a16a-6245bf024377.png)
## Эрозия
![erosion](https://user-images.githubusercontent.com/100288192/223204174-4b6fed9c-b72f-4f9d-a5a5-0d9172141823.png)
## Размыкание
![opening](https://user-images.githubusercontent.com/100288192/223204198-db7dccd9-50d7-40d7-9844-80d006f8b8c8.png)
## Замыкание
![closing](https://user-images.githubusercontent.com/100288192/223204215-7105b6d9-270f-493d-a145-df5781a39ee9.png)
## "Чёрная шляпа"
![black_hat](https://user-images.githubusercontent.com/100288192/223204247-3d52fae1-7541-4ea9-9d75-e0669b8eee3f.png)
## "Верх шляпы"
![top_hat](https://user-images.githubusercontent.com/100288192/223204276-38d0649a-79a6-4338-a34a-df1c2382ee50.png)
## Grad
![grad](https://user-images.githubusercontent.com/100288192/223203290-7052dfd2-1d8d-4813-aa36-8372ac1f6eb4.png)
## Тиснение
![emboss](https://user-images.githubusercontent.com/100288192/223201044-e8bfc7d3-624e-463b-b824-b8e548cfd3ac.png)
## Светящиеся края
![glowing_edges](https://user-images.githubusercontent.com/100288192/223201089-853673d9-8cb7-4377-84fc-9f489f0e864a.png)
## Повышение резкости 1
![increase_sharpness_1](https://user-images.githubusercontent.com/100288192/223201168-54a357bf-636f-4338-81d6-f5511dde212c.png)
## Повышение резкости 2
![increase_sharpness_2](https://user-images.githubusercontent.com/100288192/223201219-5dc57214-3472-4f6a-a0d2-fc7b411e08da.png)
## Фильтр максимума
![maximum](https://user-images.githubusercontent.com/100288192/223201350-34860dc2-6387-4f28-94bb-d873fa9ff131.png)
## Медианный фильтр
![median](https://user-images.githubusercontent.com/100288192/223215463-8ba38211-b421-4c3d-8352-38c113ca58ac.png)
## Усреднение яркости
![average_color](https://user-images.githubusercontent.com/100288192/223215482-40dcbd1f-0e32-48e0-bcd1-3c3ab5236083.png)
## Зетемнение
![darken](https://user-images.githubusercontent.com/100288192/223215539-59ef7b3f-c99a-46df-bf92-e6cee94b4d17.png)
## "Серый мир"
![gray_world](https://user-images.githubusercontent.com/100288192/223215605-3a9294bd-4326-434a-9a37-56dad285630a.png)
## Осветление
![lighten](https://user-images.githubusercontent.com/100288192/223215663-44a16cb8-0766-4fd4-b586-d71a85aac92d.png)
## Коррекция "autolevels"
![autolevels](https://user-images.githubusercontent.com/100288192/223216182-3b55e5bd-486d-4f3a-90a0-952920d4a361.png)
## Коррекция с опорным цветом
![correct_with_reference_color](https://user-images.githubusercontent.com/100288192/223216205-b8004778-b67a-4de3-b0dd-c7c002cbb61b.png)
## Линейное растяжение
![linear_stretch](https://user-images.githubusercontent.com/100288192/223216249-eead644e-87a9-457f-99b9-daaa016fe085.png)
